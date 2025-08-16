import streamlit as st
import os
import json
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from src.team.team import ATSAgentTeam
from src.config.docker_utils import DockerUtils
from src.tools.extractor_tool import FileTextExtractor
from src.tools.db_tool import DBTool

st.set_page_config(page_title="ATS Resume Analysis", layout="wide")
st.title("ATS Resume Analysis")
st.subheader("Upload your resume and select a use case")

if not os.path.exists("docs"):
    os.makedirs("docs")

files = st.file_uploader("Upload your resume", type=["pdf", "docx"], accept_multiple_files=True)
usecase = st.selectbox("Select a use case", ["New User", "Existing User"])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

if usecase == "New User":
    async def run(team, docker, task):
        try:
            conn = DBTool().connect_to_superbase(DBTool.DB_NAME, DBTool.USER, DBTool.PASSWORD, DBTool.HOST, DBTool.PORT)
            print("Connected to DB",conn)
            docker_utils = DockerUtils(docker=docker)
            await docker_utils.start_docker_container()
            async for message in team.run_stream(task=task):
                if isinstance(message, TextMessage):
                    msg = f"{message.source}: {message.content}"
                    last_message = message.content
                    print(msg, flush=True)
                    if message.source == "text_extractor_agent":
                        parsed_data = json.loads(last_message)
                        print(parsed_data)
                        DBTool().save_resume_to_db(conn, parsed_data)
                        print("Data added to database")
                        print(DBTool.ids)
                    elif message.source == "job_description_agent":
                        parsed_data = json.loads(last_message)
                        print(parsed_data)
                        DBTool().save_jobs_to_db(parsed_data, conn, DBTool.ids[-1])
                        print("Job description added to database")
                        print(DBTool.ids[-1])
                    elif message.source == "ats_scoring_agent":
                        parsed_data = json.loads(last_message)
                        DBTool.send_ats_score(parsed_data, conn, DBTool.ids[-1])
                        print("ATS score added to database")
                        print(DBTool.ids[-1])
                    elif message.source == "improvement_agent":
                        DBTool.send_improvement_to_score(message.content, conn, DBTool.ids[-1])
                        print("Improvement added to database")
                        print(DBTool.ids[-1])
                    yield msg
                elif isinstance(message, TaskResult):
                    msg = f"Stop Reason: {message.stop_reason}"
                    print(msg, flush=True)
                    yield msg

        except Exception as e:
            msg = f"Error: {str(e)}"
            print(msg, flush=True)
            yield msg
        finally:
            await docker_utils.stop_docker_container()


if st.button("Submit"):

    if usecase == "New User":
        team,docker = ATSAgentTeam().get_team()

        for file in files:
            with open(os.path.join("docs", file.name), "wb") as f:
                f.write(file.getbuffer())

        content = FileTextExtractor(file_path=os.path.join("docs", file.name)).extract_text()
        task = f"The user resume is {content}"

        async def collect_messages():
            async for msg in run(team=team, docker=docker, task=task):
                if isinstance(msg, str):
                    st.session_state.chat_history.append({"role": "assistant", "content": msg})
                    with st.chat_message("assistant"):
                        st.markdown(msg)
                elif isinstance(msg, TaskResult):
                    st.session_state.chat_history.append({"role": "assistant", "content": msg.stop_reason})
                    with st.chat_message("assistant"):
                        st.markdown(msg.stop_reason)
            img_path = "temp/combined_charts.png"
            if os.path.exists(img_path):
                st.image(img_path, caption="Combined Charts", use_container_width=True)

        asyncio.run(collect_messages())

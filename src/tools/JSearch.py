import requests
from src.config.constant import JSEARCH_API

class JSearch:
    def __init__(self):
        self.api = JSEARCH_API
    
    def JSearchAPI(self,query:str="Python Developer")->str:
        """The tool searches for job based on the query"""
        url = "https://jsearch.p.rapidapi.com/search"
        headers = {
        'x-rapidapi-key':self.api,
        'x-rapidapi-host': "jsearch.p.rapidapi.com"
        }

        params = {
            "query":query,
            "country":"in",
            "num_pages":1,
            "page":1,
        }

        response = requests.get(url,headers=headers,params=params)
        data = response.json()

        jobs = []
        for job in data.get("data", [])[:5]:
            jobs.append({
                "role": job.get("job_title"),
                "company": job.get("employer_name"),
                "employment_type": job.get("job_employment_type"),
                "job_location": job.get("job_location"),
            
                "job_salary": f"{job.get('job_min_salary')} - {job.get('job_max_salary')} {job.get('job_salary_period') or ''}".strip(),
                "job_description": job.get("job_description", ""),
                "job_apply_link": job.get("job_apply_link", "")
            })
        return jobs


calling = JSearch().JSearchAPI("python developer")
print(calling)
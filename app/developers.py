from fastapi.params import Body
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


router= APIRouter(prefix="/developers",
    tags=['Developers Details'])

# This path shows all the developers of the *Sociome* with their github accounts 
@router.get("/")
def read_item():
    return {1:{"Name": "Abhishek Kushwaha", "Github_id": "https://github.com/Abbhiishek"},
    2:{"Name": "Amandeep Singh", "Github_id": "https://github.com/Aman8017k"},
    3:{"Name": "Shivam Basak", "Github_id": "https://github.com/shivamBasak"},
    4:{"Name": "Anjali Gupta", "Github_id": "https://github.com/anjalig18"},
    5:{"Name": "Anshita Choubey", "Github_id": "https://github.com/Anshitachoubey07"},
    6:{"Name": "Muskaan Purkait Alam", "Github_id": "https://github.com/Muskaanpurkait"},
    7:{"Name": "Priya Singh", "Github_id": "https://github.com/Priyasinghjis"},
    8:{"Name": "Roshimkana Pal", "Github_id": "https://github.com/Abbhiishek"},
    9:{"Name": "Koushik Das", "Github_id": "https://github.com/koushik-das123"},
    }

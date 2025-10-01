import axios from "axios";

const API_URL = "http://localhost:8000"; // FastAPI backend

export async function getRecipes() {
  const res = await axios.get(`${API_URL}/recipes`);
  return res.data;
}

import axios from "axios";

const api = axios.create({
  baseURL: "https://ai-plant-disease-detection-system-1.onrender.com", // Change this after deploying backend
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
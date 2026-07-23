import axios from "axios";

const API_URL = "https://YOUR-RENDER-URL.onrender.com";

const getAuthHeaders = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});

export const getHistory = async () => {
  return await axios.get(`${API_URL}/history`, getAuthHeaders());
};

export const deleteHistoryRecord = async (predictionId) => {
  return await axios.delete(`${API_URL}/history/${predictionId}`, getAuthHeaders());
};
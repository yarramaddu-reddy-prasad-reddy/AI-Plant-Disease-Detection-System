import api from "./api";

const getAuthHeaders = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
  },
});

export const getHistory = async () => {
  return await api.get("/history", getAuthHeaders());
};

export const deleteHistoryRecord = async (predictionId) => {
  return await api.delete(`/history/${predictionId}`, getAuthHeaders());
};
import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

const getAuthHeaders = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
    "Content-Type": "application/json"
  },
});

export const getProfile = async () => {
  return await axios.get(`${API_URL}/profile`, getAuthHeaders());
};

export const updateProfile = async (data) => {
  return await axios.put(`${API_URL}/profile`, data, getAuthHeaders());
};

export const changePassword = async (data) => {
  return await axios.put(`${API_URL}/change-password`, data, getAuthHeaders());
};
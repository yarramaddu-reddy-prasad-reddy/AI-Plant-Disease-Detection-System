import api from "./api";

const getAuthHeaders = () => ({
  headers: {
    Authorization: `Bearer ${localStorage.getItem("token")}`,
    "Content-Type": "application/json",
  },
});

export const getProfile = async () => {
  return await api.get("/profile", getAuthHeaders());
};

export const updateProfile = async (data) => {
  return await api.put("/profile", data, getAuthHeaders());
};

export const changePassword = async (data) => {
  return await api.put("/change-password", data, getAuthHeaders());
};
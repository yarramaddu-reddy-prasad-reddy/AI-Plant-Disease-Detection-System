import api from "./api";

// Register
export const registerUser = (data) => {
    return api.post("/register", data);
};

// Login
export const loginUser = (data) => {
    return api.post("/login", data);
};
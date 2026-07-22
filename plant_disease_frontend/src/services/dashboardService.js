import api from "./api";

export const getDashboardData = () => {

    return api.get("/dashboard", {

        headers: {

            Authorization: `Bearer ${localStorage.getItem("token")}`

        }

    });

};
import { useEffect, useState } from "react";

import Layout from "../../components/Layout/Layout";
import DashboardCards from "../../components/DashboardCards/DashboardCards";

import { getDashboardData } from "../../services/dashboardService";

import "./Dashboard.css";

function Dashboard() {

    const user = JSON.parse(localStorage.getItem("user"));

    const [stats, setStats] = useState({
        total_predictions: 0,
        healthy_plants: 0,
        diseased_plants: 0,
        accuracy: 0
    });

    useEffect(() => {

        console.log("================================");
        console.log("Logged User :", user);
        console.log("Token :", localStorage.getItem("token"));
        console.log("================================");

        fetchDashboard();

    }, []);

    const fetchDashboard = async () => {

        try {

            const response = await getDashboardData();

            console.log("========== DASHBOARD API ==========");
            console.log(response.data);
            console.log("===================================");

            setStats({
                total_predictions: Number(response.data.total_predictions) || 0,
                healthy_plants: Number(response.data.healthy_plants) || 0,
                diseased_plants: Number(response.data.diseased_plants) || 0,
                accuracy: Number(response.data.accuracy) || 0
            });

        }
        catch (error) {

            console.log("========== DASHBOARD ERROR ==========");
            console.log(error);
            console.log(error.response);
            console.log("=====================================");

        }

    };

    return (

        <Layout>

            {/* Welcome Card */}

            <div className="welcome-card">

                <h1>
                    Welcome Back, {user?.full_name} 👋
                </h1>

                <p>
                    AI Powered Plant Disease Detection System
                </p>

            </div>

            {/* Statistics */}

            <div className="stats">

                <div className="stat-card stat-blue">

                    <h2>Total Predictions</h2>

                    <h1>{stats.total_predictions}</h1>

                </div>

                <div className="stat-card stat-green">

                    <h2>Healthy Plants</h2>

                    <h1>{stats.healthy_plants}</h1>

                </div>

                <div className="stat-card stat-red">

                    <h2>Diseased Plants</h2>

                    <h1>{stats.diseased_plants}</h1>

                </div>

                <div className="stat-card stat-yellow">

                    <h2>Accuracy</h2>

                    <h1>{stats.accuracy.toFixed(2)}%</h1>

                </div>

            </div>

            <DashboardCards />

        </Layout>

    );

}

export default Dashboard;
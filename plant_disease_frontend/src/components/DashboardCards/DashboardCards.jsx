import {
    MdScience,
    MdHistory,
    MdPerson,
    MdLogout
} from "react-icons/md";

import { useNavigate } from "react-router-dom";

import "./DashboardCards.css";

function DashboardCards() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.clear();

        navigate("/");

    };

    return (

        <>

            <h2 className="section-title">

                ⚡ Quick Actions

            </h2>

            <div className="action-grid">

                <div
                    className="action-card"
                    onClick={() => navigate("/predict")}
                >

                    <MdScience className="card-icon"/>

                    <h3>Disease Prediction</h3>

                    <p>

                        Upload a leaf image and detect diseases instantly.

                    </p>

                </div>

                <div
                    className="action-card"
                    onClick={() => navigate("/history")}
                >

                    <MdHistory className="card-icon"/>

                    <h3>Prediction History</h3>

                    <p>

                        View all previous AI predictions.

                    </p>

                </div>

                <div
                    className="action-card"
                    onClick={() => navigate("/profile")}
                >

                    <MdPerson className="card-icon"/>

                    <h3>Profile</h3>

                    <p>

                        Update your personal information.

                    </p>

                </div>

                <div
                    className="action-card logout-card"
                    onClick={logout}
                >

                    <MdLogout className="card-icon"/>

                    <h3>Logout</h3>

                    <p>

                        Securely sign out of your account.

                    </p>

                </div>

            </div>

        </>

    );

}

export default DashboardCards;
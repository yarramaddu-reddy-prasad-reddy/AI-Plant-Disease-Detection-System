import {
  MdDashboard,
  MdOutlineScience,
  MdHistory,
  MdPerson,
  MdLogout,
} from "react-icons/md";

import { NavLink, useNavigate } from "react-router-dom";
import "./Sidebar.css";

function Sidebar() {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <aside className="sidebar">

      <div className="logo">

        <span className="logo-icon">🌿</span>

        <div>

          <h2>Plant AI</h2>

          <p>Disease Detection</p>

        </div>

      </div>

      <nav className="menu">

        <NavLink to="/dashboard">
          <MdDashboard />
          Dashboard
        </NavLink>

        <NavLink to="/predict">
          <MdOutlineScience />
          Disease Prediction
        </NavLink>

        <NavLink to="/history">
          <MdHistory />
          Prediction History
        </NavLink>

        <NavLink to="/profile">
          <MdPerson />
          Profile
        </NavLink>

      </nav>

      <div className="bottom">

        <button onClick={logout}>
          <MdLogout />
          Logout
        </button>

        <p>Version 1.0</p>

      </div>

    </aside>
  );
}

export default Sidebar;
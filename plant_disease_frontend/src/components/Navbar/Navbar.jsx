import "./Navbar.css";

function Navbar({ onMenuClick }) {
  const user = JSON.parse(localStorage.getItem("user"));

  return (
    <div className="navbar">
      <button className="menu-toggle" onClick={onMenuClick} aria-label="Open menu">
        ☰
      </button>

      <div className="navbar-content">
        <h2>Welcome, {user?.full_name || "Guest"} 👋</h2>
        <p>{new Date().toDateString()}</p>
      </div>
    </div>
  );
}

export default Navbar;

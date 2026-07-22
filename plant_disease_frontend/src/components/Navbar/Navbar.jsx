import "./Navbar.css";

function Navbar() {
  const user = JSON.parse(localStorage.getItem("user"));

  return (
    <div className="navbar">
      <h2>Welcome, {user?.full_name} 👋</h2>

      <p>{new Date().toDateString()}</p>
    </div>
  );
}

export default Navbar;
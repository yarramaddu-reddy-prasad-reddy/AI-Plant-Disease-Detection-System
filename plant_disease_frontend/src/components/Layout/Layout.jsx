import { useState } from "react";
import Sidebar from "../Sidebar/Sidebar";
import Navbar from "../Navbar/Navbar";
import "./Layout.css";

function Layout({ children }) {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => setSidebarOpen((value) => !value);
  const closeSidebar = () => setSidebarOpen(false);

  return (
    <div className={`app-shell ${sidebarOpen ? "sidebar-open" : ""}`}>
      <Sidebar isOpen={sidebarOpen} onClose={closeSidebar} />
      <div className="sidebar-backdrop" onClick={closeSidebar} />

      <div className="main-wrapper">
        <Navbar onMenuClick={toggleSidebar} />
        <div className="content-wrapper">{children}</div>
      </div>
    </div>
  );
}

export default Layout;

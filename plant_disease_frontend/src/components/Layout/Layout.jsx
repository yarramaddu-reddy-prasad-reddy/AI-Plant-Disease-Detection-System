import Sidebar from "../Sidebar/Sidebar";
import Navbar from "../Navbar/Navbar";

function Layout({ children }) {
  return (
    <>
      <Sidebar />

      <div
        style={{
          marginLeft: "270px",
          minHeight: "100vh",
          background: "#F5FFF7",
        }}
      >
        <Navbar />

        <div style={{ padding: "35px" }}>
          {children}
        </div>
      </div>
    </>
  );
}

export default Layout;
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Layout from "../../components/Layout/Layout";
import { getProfile, updateProfile, changePassword } from "../../services/profileService";
import "./Profile.css";

function Profile() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [pageError, setPageError] = useState("");

  // Modal States
  const [showEditModal, setShowEditModal] = useState(false);
  const [showPasswordModal, setShowPasswordModal] = useState(false);

  // Edit Profile Form State
  const [editForm, setEditForm] = useState({ full_name: "", email: "" });

  // Change Password Form State
  const [passForm, setPassForm] = useState({
    current_password: "",
    new_password: "",
    confirm_password: "",
  });

  const [formError, setFormError] = useState("");
  const [formSuccess, setFormSuccess] = useState("");

  useEffect(() => {
    fetchProfileData();
  }, []);

  const fetchProfileData = async () => {
    try {
      setLoading(true);
      setPageError("");
      const response = await getProfile();
      setProfile(response.data);
      setEditForm({
        full_name: response.data.full_name,
        email: response.data.email,
      });
    } catch (error) {
      console.error("Error fetching profile:", error);
      setPageError("Unable to load profile. Please login again.");
    } finally {
      setLoading(false);
    }
  };

  // Logout Handler
  const handleLogout = () => {
    if (window.confirm("Are you sure you want to log out?")) {
      localStorage.removeItem("token");
      navigate("/login");
    }
  };

  // Save Edit Profile
  const handleUpdateProfile = async (e) => {
    e.preventDefault();
    setFormError("");
    setFormSuccess("");

    try {
      await updateProfile(editForm);
      setFormSuccess("Profile updated successfully!");
      fetchProfileData();
      setTimeout(() => {
        setShowEditModal(false);
        setFormSuccess("");
      }, 1200);
    } catch (error) {
      setFormError(error.response?.data?.error || "Failed to update profile");
    }
  };

  // Change Password
  const handleChangePassword = async (e) => {
    e.preventDefault();
    setFormError("");
    setFormSuccess("");

    if (passForm.new_password !== passForm.confirm_password) {
      setFormError("New passwords do not match!");
      return;
    }

    try {
      await changePassword({
        current_password: passForm.current_password,
        new_password: passForm.new_password,
      });
      setFormSuccess("Password updated successfully!");
      setPassForm({ current_password: "", new_password: "", confirm_password: "" });
      setTimeout(() => {
        setShowPasswordModal(false);
        setFormSuccess("");
      }, 1200);
    } catch (error) {
      setFormError(error.response?.data?.error || "Failed to change password");
    }
  };

  if (loading) {
    return (
      <Layout>
        <div className="profile-loading">
          <div className="spinner"></div>
          <p>Fetching user details...</p>
        </div>
      </Layout>
    );
  }

  if (!profile) {
    return (
      <Layout>
        <div className="profile-loading">
          <p>{pageError || "Profile information is unavailable."}</p>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="profile-page">
        {/* Main Banner Card */}
        <div className="profile-card">
          <div className="avatar">👤</div>
          <h2>{profile.full_name}</h2>
          <p>{profile.email}</p>
          <span className="role-badge">{profile.role || "User"}</span>
        </div>

        {/* Info Card */}
        <div className="info-card">
          <h2>Personal Information</h2>
          <div className="info-row">
            <strong>User ID</strong>
            <span>#{profile.user_id}</span>
          </div>
          <div className="info-row">
            <strong>Full Name</strong>
            <span>{profile.full_name}</span>
          </div>
          <div className="info-row">
            <strong>Email</strong>
            <span>{profile.email}</span>
          </div>
          <div className="info-row">
            <strong>Member Since</strong>
            <span>
              {profile.created_at
                ? new Date(profile.created_at).toLocaleDateString("en-US", {
                    month: "long",
                    day: "numeric",
                    year: "numeric",
                  })
                : "N/A"}
            </span>
          </div>
        </div>

        {/* Prediction Statistics */}
        <h2 className="section-title">Prediction Statistics</h2>
        <div className="stats-grid">
          <div className="stat blue">
            <h3>Total Predictions</h3>
            <h1>{profile.total_predictions}</h1>
          </div>
          <div className="stat green">
            <h3>Healthy Plants</h3>
            <h1>{profile.healthy_plants}</h1>
          </div>
          <div className="stat red">
            <h3>Diseased Plants</h3>
            <h1>{profile.diseased_plants}</h1>
          </div>
          <div className="stat orange">
            <h3>Avg Accuracy</h3>
            <h1>{profile.accuracy}%</h1>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="button-group">
          <button className="edit-btn" onClick={() => setShowEditModal(true)}>
            ✏️ Edit Profile
          </button>
          <button className="password-btn" onClick={() => setShowPasswordModal(true)}>
            🔒 Change Password
          </button>
          <button className="logout-btn" onClick={handleLogout}>
            🚪 Logout
          </button>
        </div>

        {/* Modal: Edit Profile */}
        {showEditModal && (
          <div className="modal-overlay" onClick={() => setShowEditModal(false)}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>Edit Profile</h3>
                <button className="close-btn" onClick={() => setShowEditModal(false)}>
                  ✕
                </button>
              </div>
              <form onSubmit={handleUpdateProfile}>
                {formError && <div className="alert-box error">{formError}</div>}
                {formSuccess && <div className="alert-box success">{formSuccess}</div>}

                <div className="input-group">
                  <label>Full Name</label>
                  <input
                    type="text"
                    required
                    value={editForm.full_name}
                    onChange={(e) =>
                      setEditForm({ ...editForm, full_name: e.target.value })
                    }
                  />
                </div>

                <div className="input-group">
                  <label>Email Address</label>
                  <input
                    type="email"
                    required
                    value={editForm.email}
                    onChange={(e) =>
                      setEditForm({ ...editForm, email: e.target.value })
                    }
                  />
                </div>

                <div className="modal-actions">
                  <button type="submit" className="save-btn">
                    Save Changes
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Modal: Change Password */}
        {showPasswordModal && (
          <div className="modal-overlay" onClick={() => setShowPasswordModal(false)}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>Change Password</h3>
                <button
                  className="close-btn"
                  onClick={() => setShowPasswordModal(false)}
                >
                  ✕
                </button>
              </div>
              <form onSubmit={handleChangePassword}>
                {formError && <div className="alert-box error">{formError}</div>}
                {formSuccess && <div className="alert-box success">{formSuccess}</div>}

                <div className="input-group">
                  <label>Current Password</label>
                  <input
                    type="password"
                    required
                    value={passForm.current_password}
                    onChange={(e) =>
                      setPassForm({ ...passForm, current_password: e.target.value })
                    }
                  />
                </div>

                <div className="input-group">
                  <label>New Password</label>
                  <input
                    type="password"
                    required
                    value={passForm.new_password}
                    onChange={(e) =>
                      setPassForm({ ...passForm, new_password: e.target.value })
                    }
                  />
                </div>

                <div className="input-group">
                  <label>Confirm New Password</label>
                  <input
                    type="password"
                    required
                    value={passForm.confirm_password}
                    onChange={(e) =>
                      setPassForm({ ...passForm, confirm_password: e.target.value })
                    }
                  />
                </div>

                <div className="modal-actions">
                  <button type="submit" className="save-btn">
                    Update Password
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
}

export default Profile;
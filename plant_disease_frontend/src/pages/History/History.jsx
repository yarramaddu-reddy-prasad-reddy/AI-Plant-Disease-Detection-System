import React, { useEffect, useState, useMemo } from "react";
import Layout from "../../components/Layout/Layout";
import { getHistory, deleteHistoryRecord } from "../../services/historyService";
import "./History.css";

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  
  // Filters state
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("ALL");
  const [plantFilter, setPlantFilter] = useState("ALL");
  
  // Modal State
  const [selectedItem, setSelectedItem] = useState(null);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    try {
      setLoading(true);
      const response = await getHistory();
      setHistory(response.data);
    } catch (error) {
      console.error("Error fetching history:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    if (!window.confirm("Are you sure you want to delete this prediction record?")) return;
    
    try {
      await deleteHistoryRecord(id);
      setHistory((prev) => prev.filter((item) => item.prediction_id !== id));
      if (selectedItem?.prediction_id === id) setSelectedItem(null);
    } catch (error) {
      alert("Failed to delete record.");
      console.error(error);
    }
  };

  // Extract unique plant names for the drop-down filter
  const uniquePlants = useMemo(() => {
    const plants = history.map((i) => i.plant_name);
    return ["ALL", ...Array.from(new Set(plants))];
  }, [history]);

  // Analytics Calculations
  const stats = useMemo(() => {
    const total = history.length;
    const healthyCount = history.filter((i) => i.status === "Healthy").length;
    const diseasedCount = total - healthyCount;
    return { total, healthyCount, diseasedCount };
  }, [history]);

  // Filtered List
  const filteredHistory = useMemo(() => {
    return history.filter((item) => {
      const matchesSearch =
        item.plant_name.toLowerCase().includes(search.toLowerCase()) ||
        item.disease_name.toLowerCase().includes(search.toLowerCase());

      const matchesStatus =
        statusFilter === "ALL" || item.status.toUpperCase() === statusFilter;

      const matchesPlant =
        plantFilter === "ALL" || item.plant_name === plantFilter;

      return matchesSearch && matchesStatus && matchesPlant;
    });
  }, [history, search, statusFilter, plantFilter]);

  return (
    <Layout>
      <div className="history-container">
        <div className="history-header">
          <h1>📜 Prediction History</h1>
          <p>View, filter, and review all your previous plant diagnostic scans</p>
        </div>

        {/* Top Summary Statistics Cards */}
        <div className="stats-grid">
          <div className="stat-card">
            <span className="stat-icon">📊</span>
            <div>
              <h3>{stats.total}</h3>
              <p>Total Scans</p>
            </div>
          </div>
          <div className="stat-card healthy-border">
            <span className="stat-icon">🌱</span>
            <div>
              <h3>{stats.healthyCount}</h3>
              <p>Healthy Plants</p>
            </div>
          </div>
          <div className="stat-card diseased-border">
            <span className="stat-icon">⚠️</span>
            <div>
              <h3>{stats.diseasedCount}</h3>
              <p>Diseased Plants</p>
            </div>
          </div>
        </div>

        {/* Filter Controls Bar */}
        <div className="filter-bar">
          <input
            type="text"
            placeholder="🔍 Search plant or disease name..."
            className="search-input"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />

          <select
            className="filter-select"
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
          >
            <option value="ALL">All Statuses</option>
            <option value="HEALTHY">Healthy Only</option>
            <option value="DISEASED">Diseased Only</option>
          </select>

          <select
            className="filter-select"
            value={plantFilter}
            onChange={(e) => setPlantFilter(e.target.value)}
          >
            {uniquePlants.map((plant) => (
              <option key={plant} value={plant}>
                {plant === "ALL" ? "All Plant Types" : plant}
              </option>
            ))}
          </select>
        </div>

        {/* Data Table */}
        <div className="history-table-container">
          <table className="history-table">
            <thead>
              <tr>
                <th>Image</th>
                <th>Plant</th>
                <th>Disease</th>
                <th>Status</th>
                <th>Confidence</th>
                <th>Scan Date</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr>
                  <td colSpan="7" className="table-message">
                    Loading history...
                  </td>
                </tr>
              ) : filteredHistory.length === 0 ? (
                <tr>
                  <td colSpan="7" className="table-message">
                    No prediction records found matching your filters.
                  </td>
                </tr>
              ) : (
                filteredHistory.map((item) => (
                  <tr key={item.prediction_id}>
                    <td>
                      <img
                        src={item.image_url}
                        alt="Leaf scan"
                        className="history-thumb"
                      />
                    </td>
                    <td><strong>{item.plant_name}</strong></td>
                    <td>{item.disease_name}</td>
                    <td>
                      <span className={`status-pill ${item.status.toLowerCase()}`}>
                        {item.status}
                      </span>
                    </td>
                    <td>
                      <div className="confidence-wrapper">
                        <span>{item.confidence}%</span>
                      </div>
                    </td>
                    <td>
                      {new Date(item.prediction_time).toLocaleString("en-US", {
                        dateStyle: "medium",
                        timeStyle: "short",
                      })}
                    </td>
                    <td>
                      <div className="action-buttons">
                        <button
                          className="btn-view"
                          onClick={() => setSelectedItem(item)}
                        >
                          Details
                        </button>
                        <button
                          className="btn-delete"
                          onClick={() => handleDelete(item.prediction_id)}
                        >
                          🗑️
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>

        {/* Details Modal */}
        {selectedItem && (
          <div className="modal-overlay" onClick={() => setSelectedItem(null)}>
            <div className="modal-card" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h2>{selectedItem.plant_name} — {selectedItem.disease_name}</h2>
                <button className="close-btn" onClick={() => setSelectedItem(null)}>
                  ✕
                </button>
              </div>

              <div className="modal-body">
                <div className="modal-image-col">
                  <img src={selectedItem.image_url} alt="Scan leaf" />
                  <div className="modal-meta">
                    <p><strong>Confidence:</strong> {selectedItem.confidence}%</p>
                    <p><strong>Status:</strong> {selectedItem.status}</p>
                    <p>
                      <strong>Scanned:</strong>{" "}
                      {new Date(selectedItem.prediction_time).toLocaleString()}
                    </p>
                  </div>
                </div>

                <div className="modal-info-col">
                  {selectedItem.details?.description && (
                    <div className="info-block">
                      <h4>Description</h4>
                      <p>{selectedItem.details.description}</p>
                    </div>
                  )}
                  {selectedItem.details?.treatment && (
                    <div className="info-block">
                      <h4>Treatment</h4>
                      <p>{selectedItem.details.treatment}</p>
                    </div>
                  )}
                  {selectedItem.details?.prevention && (
                    <div className="info-block">
                      <h4>Prevention</h4>
                      <p>{selectedItem.details.prevention}</p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </Layout>
  );
}

export default History;
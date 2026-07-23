import React, { useState, useRef } from "react";
import Layout from "../../components/Layout/Layout";
import api from "../../services/api";
import { useToast } from "../../components/Toast/ToastProvider";
import "./Predict.css";

function Predict() {
  const { addToast } = useToast();
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [activeTab, setActiveTab] = useState("overview");
  const [isDragging, setIsDragging] = useState(false);

  const fileInputRef = useRef(null);

  const processFile = (file) => {
    if (!file || !file.type.startsWith("image/")) {
      addToast("Please upload a valid image file.", "error");
      return;
    }

    setImage(file);

    if (preview) {
      URL.revokeObjectURL(preview);
    }

    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    processFile(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0]);
    }
  };

  const handlePredict = async () => {
    if (!image) {
      addToast("Please select or drop an image first.", "error");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      setLoading(true);

      const response = await api.post(
        "/predict",
        formData,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);

    } catch (error) {
      console.error(error);

      addToast(
        error.response?.data?.error || "Prediction Failed",
        "error"
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <div className="predict-container">

        <h1 className="predict-title">
          🌿 Plant Health Analyzer
        </h1>

        <div className="upload-card">

          <div
            className={`upload-box ${isDragging ? "dragging" : ""}`}
            onClick={() => fileInputRef.current.click()}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
          >

            {preview ? (
              <img
                src={preview}
                alt="Leaf Preview"
                className="preview-image"
              />
            ) : (
              <div className="upload-placeholder">

                <div className="upload-icon">
                  📷
                </div>

                <div className="upload-text">
                  Drag & Drop or Click to Upload
                </div>

                <div className="upload-sub">
                  Supports PNG, JPG, JPEG
                </div>

              </div>
            )}

            <input
              type="file"
              ref={fileInputRef}
              accept="image/*"
              onChange={handleImageChange}
              className="file-input"
            />

          </div>

          <button
            className="predict-btn"
            onClick={handlePredict}
            disabled={loading || !image}
          >

            {loading ? (
              <span className="spinner-text">
                Analyzing Leaf...
              </span>
            ) : (
              "Diagnose Plant"
            )}

          </button>

        </div>

        {result && (

          <div className="result-card">

            <div className="result-header">

              <div>

                <span className="badge-plant">
                  {result.plant_name}
                </span>

                <h2 className="disease-title">
                  {result.disease_name}
                </h2>

              </div>

              <div className="confidence-badge">

                <div className="confidence-score">
                  {result.confidence}%
                </div>

                <div className="confidence-label">
                  {result.confidence_level} Confidence
                </div>

              </div>

            </div>

            <div className="severity-bar-container">

              <span className="severity-label">
                Status: <strong>{result.status}</strong>
              </span>

              <span className="severity-label">
                Severity: <strong>{result.disease_severity}</strong>
              </span>

            </div>

            <div className="result-tabs">

              <button
                className={`tab-btn ${activeTab === "overview" ? "active" : ""}`}
                onClick={() => setActiveTab("overview")}
              >
                🔍 Summary
              </button>

              <button
                className={`tab-btn ${activeTab === "treatment" ? "active" : ""}`}
                onClick={() => setActiveTab("treatment")}
              >
                💊 Care & Treatment
              </button>

              <button
                className={`tab-btn ${activeTab === "prevention" ? "active" : ""}`}
                onClick={() => setActiveTab("prevention")}
              >
                🛡️ Prevention
              </button>

            </div>

            <div className="tab-content">

              {activeTab === "overview" && (

                <div className="info-grid">

                  <div className="info-box full-width">

                    <h4>Description</h4>

                    <p>{result.description}</p>

                  </div>

                </div>

              )}

              {activeTab === "treatment" && (

                <div className="info-grid">

                  <div className="info-box">

                    <h4>Standard Treatment</h4>

                    <p>{result.treatment}</p>

                  </div>

                  <div className="info-box">

                    <h4>Recommended Pesticide</h4>

                    <p>{result.recommended_pesticide}</p>

                  </div>

                  <div className="info-box">

                    <h4>Organic Solution</h4>

                    <p>{result.organic_solution}</p>

                  </div>

                </div>

              )}

              {activeTab === "prevention" && (

                <div className="info-grid">

                  <div className="info-box">

                    <h4>Prevention Steps</h4>

                    <p>{result.prevention}</p>

                  </div>

                  <div className="info-box">

                    <h4>Watering Advice</h4>

                    <p>{result.watering_advice}</p>

                  </div>

                  <div className="info-box">

                    <h4>Fertilizer Recommendation</h4>

                    <p>{result.fertilizer_recommendation}</p>

                  </div>

                </div>

              )}

            </div>

          </div>

        )}

      </div>
    </Layout>
  );
}

export default Predict;
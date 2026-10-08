import { useState } from "react";
import axios from "axios";
import "../styles/Generate.css";

function Generate() {
  const [formData, setFormData] = useState({
    degree: "",
    university: "",
    discipline: "",
    target_journal: "",
    topic: ""
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Validation
    if (!formData.degree || !formData.university || !formData.discipline || !formData.topic) {
      setError("Please fill in all required fields");
      return;
    }

    setLoading(true);
    setError(null);
    
    try {
      const apiUrl = import.meta.env.VITE_API_URL || '/api/generate';
      console.log("Sending request to", apiUrl, "with data:", formData);
      const response = await axios.post(apiUrl, formData, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      
      console.log("Response received:", response.data);
      setResult(response.data);
    } catch (err) {
      console.error("Error:", err);
      const errorMessage = err.response?.data?.detail || err.message || 'Error generating thesis. See console.';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="generate-container">
      <div className="header">
        <h1>📘 Adaptive Thesis Generator</h1>
        <p>Generate your research thesis automatically</p>
      </div>

      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>Degree *</label>
          <select
            name="degree"
            value={formData.degree}
            onChange={handleChange}
          >
            <option value="">Select a degree</option>
            <option value="UG">Undergraduate</option>
            <option value="Master">Master's</option>
            <option value="PhD">PhD</option>
          </select>
        </div>

        <div className="form-group">
          <label>University *</label>
          <input
            type="text"
            name="university"
            value={formData.university}
            onChange={handleChange}
            placeholder="e.g., MIT, Stanford"
          />
        </div>

        <div className="form-group">
          <label>Discipline *</label>
          <input
            type="text"
            name="discipline"
            value={formData.discipline}
            onChange={handleChange}
            placeholder="e.g., Computer Science, Biology"
          />
        </div>

        <div className="form-group">
          <label>Research Topic *</label>
          <input
            type="text"
            name="topic"
            value={formData.topic}
            onChange={handleChange}
            placeholder="e.g., Machine Learning, Climate Change"
          />
        </div>

        <div className="form-group">
          <label>Target Journal (Optional)</label>
          <input
            type="text"
            name="target_journal"
            value={formData.target_journal}
            onChange={handleChange}
            placeholder="e.g., IEEE Transactions"
          />
        </div>

        {error && <div className="error-message">{error}</div>}

        <button 
          type="submit" 
          disabled={loading}
          className="submit-btn"
        >
          {loading ? '⏳ Generating…' : '✨ Generate Thesis'}
        </button>
      </form>

      {loading && (
        <div className="loading">
          <div className="spinner"></div>
          <p>Analyzing your research profile and generating thesis structure...</p>
        </div>
      )}

      {result && (
        <div className="results">
          <h2>📊 Generation Results</h2>
          
          {result.policy && (
            <div className="result-section">
              <h3>Research Policy</h3>
              <pre>{JSON.stringify(result.policy, null, 2)}</pre>
            </div>
          )}

          {result.blueprint && (
            <div className="result-section">
              <h3>Research Blueprint</h3>
              <pre>{JSON.stringify(result.blueprint, null, 2)}</pre>
            </div>
          )}

          {result.papers && (
            <div className="result-section">
              <h3>Found Papers ({result.papers.length})</h3>
              {result.papers.length > 0 ? (
                <ul>
                  {result.papers.map((paper, idx) => (
                    <li key={idx}>
                      <strong>{paper.title}</strong>
                      {paper.url && <a href={paper.url} target="_blank" rel="noopener noreferrer"> View</a>}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No papers found.</p>
              )}
            </div>
          )}

          <button onClick={() => setResult(null)} className="clear-btn">
            Clear Results
          </button>
        </div>
      )}
    </div>
  );
}

export default Generate;
import "./StatisticsCards.css";

function StatisticsCards() {

    return (

        <div className="stats-grid">

            <div className="stat-card blue">

                <h3>Total Predictions</h3>

                <h1>0</h1>

                <p>Total scans performed</p>

            </div>

            <div className="stat-card green">

                <h3>Healthy Plants</h3>

                <h1>0</h1>

                <p>Healthy detections</p>

            </div>

            <div className="stat-card red">

                <h3>Diseased Plants</h3>

                <h1>0</h1>

                <p>Disease detected</p>

            </div>

            <div className="stat-card orange">

                <h3>Accuracy</h3>

                <h1>98%</h1>

                <p>AI Prediction Accuracy</p>

            </div>

        </div>

    );

}

export default StatisticsCards;
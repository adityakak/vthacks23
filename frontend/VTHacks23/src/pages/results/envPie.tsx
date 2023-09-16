import React from "react";
import { Chart, CategoryScale, ArcElement } from "chart.js";
import { Doughnut } from "react-chartjs-2";
Chart.register(CategoryScale, ArcElement);
const envPie: React.FC = () => {
    const data = {
        labels: ["A", "B", "C"],
        datasets: [
            {
                data: [30, 40, 10, 20],
                backgroundColor: ["#FF5733", "#33FF57", "#5733FF", "#000000"],
                borderWidth: [0, 0, 0, 0],
            },
        ],
    };

    return (
        <div>
            <Doughnut
                data={data}
                options={{
                    plugins: {
                        legend: {
                            display: false, // Hide the legend
                        },
                    },
                }}
            />
        </div>
    );
};

export default envPie;

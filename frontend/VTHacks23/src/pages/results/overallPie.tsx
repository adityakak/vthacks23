import React from 'react';
import { Pie } from 'react-chartjs-2';

const overallPie: React.FC = () => {
  const data = {
    labels: ['A', 'B', 'C'],
    datasets: [
      {
        data: [30, 40, 30],
        backgroundColor: ['#FF5733', '#33FF57', '#5733FF'],
      },
    ],
  };

  return (
    <div>
      <h2>Pie Chart 1</h2>
      <Pie data={data} />
    </div>
  );
};

export default overallPie;

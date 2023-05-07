import {useState, useEffect} from 'react';
import {BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const EloRatings = () => {
  const [eloData, setEloData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://localhost:8000/api/elo');
      const data = await response.json();
      setEloData(data);
    };

    fetchData();
  }, []);

  return (
    <div>
      <ResponsiveContainer>
        <BarChart data={eloData} margin={{top: 20, right: 30, left: 20, bottom: 5}}>
          <CartesianGrid strokeDasharray="3 3" /> 
          <XAxis dataKey="team" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="rating" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
};

export default function Home() {
  return (
    <div>
      <h1>MLB Elo Rating</h1>
      <EloRatings />
    </div>
  )
}


import React, { useState, useEffect } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const Dashboard = () => {
  const [orders, setOrders] = useState([]);
  const [scaleTargets, setScaleTargets] = useState([]);
  const [niches, setNiches] = useState([]);
  const [financials, setFinancials] = useState([]);

  const fetchOrders = async () => {
    const res = await fetch("https://your-backend-url.com/orders");
    const data = await res.json();
    setOrders(data.orders || []);
  };

  const fetchScaleTargets = async () => {
    const res = await fetch("https://your-backend-url.com/scale-targets");
    const data = await res.json();
    setScaleTargets(data.targets || []);
  };

  const fetchNiches = async () => {
    const res = await fetch("https://your-backend-url.com/niches");
    const data = await res.json();
    setNiches(data.niches || []);
  };

  const fetchFinancials = async () => {
    const res = await fetch("https://your-backend-url.com/financials");
    const data = await res.json();
    setFinancials(data.metrics || []);
  };

  useEffect(() => {
    fetchOrders();
    fetchScaleTargets();
    fetchNiches();
    fetchFinancials();
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Nova Scout AI Dashboard</h1>

      <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: '10px' }}>
        <h2>Orders</h2>
        <ul>
          {orders.map((o, i) => (
            <li key={i}>
              <strong>{o.id}</strong> - {o.product} → {o.status} (Tracking: {o.tracking})
            </li>
          ))}
        </ul>
      </div>

      <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: '10px' }}>
        <h2>Scaling Recommendations (ROI%)</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={scaleTargets}>
            <XAxis dataKey="product" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="roi_percent" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: '10px' }}>
        <h2>Niche Vault</h2>
        <ul>
          {niches.map((n, i) => (
            <li key={i}>
              <strong>{n.product}</strong> | Score: {n.opportunity_score} | Supplier: {n.supplier}
            </li>
          ))}
        </ul>
      </div>

      <div style={{ marginTop: '2rem', padding: '1rem', border: '1px solid #ccc', borderRadius: '10px' }}>
        <h2>Financial Metrics</h2>
        <ul>
          {financials.map((item, i) => (
            <li key={i}>
              <strong>{item.product}</strong>: Sale ${item.sale_price?.toFixed(2)} | Cost ${item.supplier_cost?.toFixed(2)} | Profit ${item.net_profit?.toFixed(2)} | ROI {item.roi_percent?.toFixed(1)}%
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Dashboard;

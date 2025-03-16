// /frontend/src/pages/Dashboard.jsx
import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
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
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Nova Scout AI Dashboard</h1>

      <Card className="shadow-xl">
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold mb-2">Orders</h2>
          <ul className="space-y-2">
            {orders.map((o, i) => (
              <li key={i} className="border p-2 rounded-xl">
                <strong>{o.id}</strong> - {o.product} → {o.status} (Tracking: {o.tracking})
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card className="shadow-xl">
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold mb-4">Scaling Recommendations (ROI%)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={scaleTargets}>
              <XAxis dataKey="product" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="roi_percent" fill="#82ca9d" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      <Card className="shadow-xl">
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold mb-2">Niche Vault</h2>
          <ul className="space-y-2">
            {niches.map((n, i) => (
              <li key={i} className="border p-2 rounded-xl">
                <strong>{n.product}</strong> | Score: {n.opportunity_score} | Supplier: {n.supplier}
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>

      <Card className="shadow-xl">
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold mb-2">Financial Metrics</h2>
          <ul className="space-y-2">
            {financials.map((item, i) => (
              <li key={i} className="border p-2 rounded-xl">
                <strong>{item.product}</strong>: Sale ${item.sale_price?.toFixed(2)} | Cost ${item.supplier_cost?.toFixed(2)} | Profit ${item.net_profit?.toFixed(2)} | ROI {item.roi_percent?.toFixed(1)}%
              </li>
            ))}
          </ul>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;

// Dropshipping AI Dashboard Interface
// Created: 2025-03-16

import React, { useState, useEffect } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const sampleData = [
  { product: "Ergo Chair", roi: 92, netProfit: 34.5 },
  { product: "LED Desk Lamp", roi: 85, netProfit: 28.7 },
  { product: "Aroma Diffuser", roi: 78, netProfit: 21.3 }
];

const Dashboard = () => {
  const [orders, setOrders] = useState([]);
  const [scaleTargets, setScaleTargets] = useState(sampleData);

  const loadOrders = () => {
    setOrders([
      { id: "ORD1023", product: "Ergo Chair", status: "Processed", tracking: "TRK102938" },
      { id: "ORD1024", product: "LED Desk Lamp", status: "Shipped", tracking: "TRK102939" },
      { id: "ORD1025", product: "Aroma Diffuser", status: "Delivered", tracking: "TRK102940" }
    ]);
  };

  useEffect(() => {
    loadOrders();
  }, []);

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">Dropshipping AI Dashboard</h1>

      <Card className="shadow-xl">
        <CardContent className="p-4">
          <h2 className="text-xl font-semibold mb-2">Order Status</h2>
          <ul className="space-y-2">
            {orders.map((order) => (
              <li key={order.id} className="border p-2 rounded-xl">
                <strong>{order.id}</strong> - {order.product} → {order.status} (Tracking: {order.tracking})
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
              <Bar dataKey="roi" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;

'use client';

import { Bar, BarChart, ResponsiveContainer, XAxis, YAxis } from 'recharts';

const data = [
  {
    name: 'Jan',
    total: 4500,
  },
  {
    name: 'Feb',
    total: 2400,
  },
  {
    name: 'Mar',
    total: 2800,
  },
  {
    name: 'Apr',
    total: 5600,
  },
  {
    name: 'May',
    total: 2000,
  },
  {
    name: 'Jun',
    total: 4800,
  },
  {
    name: 'Jul',
    total: 4600,
  },
  {
    name: 'Aug',
    total: 4800,
  },
  {
    name: 'Sep',
    total: 1800,
  },
  {
    name: 'Oct',
    total: 4000,
  },
  {
    name: 'Nov',
    total: 3800,
  },
  {
    name: 'Dec',
    total: 4800,
  },
];

export function Overview() {
  return (
    <ResponsiveContainer width="100%" height={350}>
      <BarChart data={data}>
        <XAxis
          dataKey="name"
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false}
        />
        <YAxis
          stroke="#888888"
          fontSize={12}
          tickLine={false}
          axisLine={false}
          tickFormatter={(value) => `$${value}`}
        />
        <Bar
          dataKey="total"
          fill="#000000"
          radius={[4, 4, 0, 0]}
          className="fill-primary"
        />
      </BarChart>
    </ResponsiveContainer>
  );
}

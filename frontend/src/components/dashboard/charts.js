'use client';

import {
  LineChart,
  Line,
  AreaChart,
  Area,
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend,
  XAxis,
  YAxis,
} from 'recharts';

const lineData = [
  { name: 'Mon', visits: 2400, clicks: 1398 },
  { name: 'Tue', visits: 1398, clicks: 3400 },
  { name: 'Wed', visits: 9800, clicks: 2400 },
  { name: 'Thu', visits: 3908, clicks: 4300 },
  { name: 'Fri', visits: 4800, clicks: 6300 },
  { name: 'Sat', visits: 3800, clicks: 4300 },
  { name: 'Sun', visits: 4300, clicks: 3300 },
];

const areaData = [
  { name: 'Jan', desktop: 4000, mobile: 2400, tablet: 2400 },
  { name: 'Feb', desktop: 3000, mobile: 1398, tablet: 2210 },
  { name: 'Mar', desktop: 2000, mobile: 9800, tablet: 2290 },
  { name: 'Apr', desktop: 2780, mobile: 3908, tablet: 2000 },
  { name: 'May', desktop: 1890, mobile: 4800, tablet: 2181 },
  { name: 'Jun', desktop: 2390, mobile: 3800, tablet: 2500 },
  { name: 'Jul', desktop: 3490, mobile: 4300, tablet: 2100 },
];

const pieData = [
  { name: 'Desktop', value: 400 },
  { name: 'Mobile', value: 300 },
  { name: 'Tablet', value: 200 },
  { name: 'Other', value: 100 },
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

export function WebTrafficChart() {
  return (
    <ResponsiveContainer width="100%" height={350}>
      <LineChart data={lineData}>
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
        />
        <Tooltip />
        <Legend />
        <Line
          type="monotone"
          dataKey="visits"
          stroke="#000000"
          strokeWidth={2}
          dot={false}
          className="stroke-primary"
        />
        <Line
          type="monotone"
          dataKey="clicks"
          stroke="#888888"
          strokeWidth={2}
          dot={false}
        />
      </LineChart>
    </ResponsiveContainer>
  );
}

export function DeviceUsageChart() {
  return (
    <ResponsiveContainer width="100%" height={350}>
      <AreaChart data={areaData}>
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
        />
        <Tooltip />
        <Legend />
        <Area
          type="monotone"
          dataKey="mobile"
          stackId="1"
          stroke="#000000"
          fill="#000000"
          className="stroke-primary fill-primary"
        />
        <Area
          type="monotone"
          dataKey="desktop"
          stackId="1"
          stroke="#888888"
          fill="#888888"
          fillOpacity={0.7}
        />
        <Area
          type="monotone"
          dataKey="tablet"
          stackId="1"
          stroke="#e5e5e5"
          fill="#e5e5e5"
          fillOpacity={0.5}
        />
      </AreaChart>
    </ResponsiveContainer>
  );
}

export function DeviceDistributionChart() {
  return (
    <ResponsiveContainer width="100%" height={350}>
      <PieChart>
        <Pie
          data={pieData}
          cx="50%"
          cy="50%"
          innerRadius={60}
          outerRadius={80}
          fill="#000000"
          paddingAngle={5}
          dataKey="value"
          className="fill-primary"
        >
          {pieData.map((entry, index) => (
            <Cell
              key={`cell-${index}`}
              fill={
                index === 0
                  ? '#000000'
                  : `#888888${Math.floor((3 - index) * 0.3 * 255).toString(16)}`
              }
              className={index === 0 ? 'fill-primary' : ''}
            />
          ))}
        </Pie>
        <Tooltip />
        <Legend />
      </PieChart>
    </ResponsiveContainer>
  );
}

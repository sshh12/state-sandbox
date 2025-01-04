import {
  PieChart as RechartsPieChart,
  Pie,
  ResponsiveContainer,
  Cell,
  Legend,
  Tooltip,
} from 'recharts';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { useState } from 'react';
import { MetricLineChartDialog } from './metric-line-chart-dialog';

// Modern dark color scheme
const COLORS = [
  '#2563eb', // Blue
  '#16a34a', // Green
  '#9333ea', // Purple
  '#ea580c', // Orange
  '#0d9488', // Teal
  '#c026d3', // Pink
  '#0369a1', // Light Blue
  '#b91c1c', // Red
  '#854d0e', // Amber
  '#4338ca', // Indigo
];

const renderLegend = (props) => {
  const { payload, onClick } = props;
  return (
    <div className="grid grid-cols-2 gap-2 text-sm mt-4 px-2">
      {payload.map((entry, index) => (
        <div
          key={`item-${index}`}
          className="flex items-center gap-2 min-w-[120px] overflow-hidden cursor-pointer hover:bg-accent rounded-md p-1"
          onClick={() => onClick?.(entry)}
        >
          <div
            className="w-3 h-3 rounded-full flex-shrink-0"
            style={{ backgroundColor: entry.color }}
          />
          <span className="truncate">{entry.value}</span>
          <span className="flex-shrink-0 text-muted-foreground">
            {(entry.payload.value * 100).toFixed(1)}%
          </span>
        </div>
      ))}
    </div>
  );
};

const CustomTooltip = ({ active, payload, onClick }) => {
  if (active && payload && payload.length) {
    const data = payload[0];
    return (
      <div
        className="bg-card border border-border rounded-lg p-3 shadow-lg cursor-pointer hover:bg-accent"
        onClick={() => onClick?.(data)}
      >
        <div className="flex items-center gap-2">
          <div
            className="w-3 h-3 rounded-full"
            style={{ backgroundColor: data.payload.fill }}
          />
          <span className="font-medium">{data.name}</span>
        </div>
        <div className="mt-1 text-muted-foreground">
          {(data.value * 100).toFixed(1)}%
        </div>
      </div>
    );
  }
  return null;
};

export default function PieChartCard({
  title,
  data,
  snapshots,
  valueKeyPrefix,
  span = 2,
}) {
  const [selectedMetric, setSelectedMetric] = useState(null);
  const [showChart, setShowChart] = useState(false);

  const chartData = data.map((item, index) => ({
    name: item.key,
    value: item.value,
    fill: COLORS[index % COLORS.length],
    valueKey: `${valueKeyPrefix}.${item.key
      .toLowerCase()
      .replace(/[^a-z0-9]/g, '_')}`,
  }));

  const handleClick = (entry) => {
    setSelectedMetric({
      title: entry.payload.name || entry.name,
      valueKey: entry.payload.valueKey,
    });
    setShowChart(true);
  };

  return (
    <Card className={`col-span-${span}`}>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <ResponsiveContainer width="100%" height={350}>
          <RechartsPieChart>
            <Pie
              data={chartData}
              cx="50%"
              cy="45%"
              innerRadius={60}
              outerRadius={100}
              dataKey="value"
              paddingAngle={2}
              onClick={handleClick}
              className="cursor-pointer"
            >
              {chartData.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={entry.fill}
                  stroke="transparent"
                />
              ))}
            </Pie>
            <Tooltip
              content={<CustomTooltip onClick={handleClick} />}
              formatter={(value) => [(value * 100).toFixed(1) + '%']}
            />
            <Legend
              content={(props) =>
                renderLegend({ ...props, onClick: handleClick })
              }
            />
          </RechartsPieChart>
        </ResponsiveContainer>
      </CardContent>
      {selectedMetric && (
        <MetricLineChartDialog
          isOpen={showChart}
          onOpenChange={setShowChart}
          title={`${title} - ${selectedMetric.title}`}
          snapshots={snapshots}
          valueKey={selectedMetric.valueKey}
        />
      )}
    </Card>
  );
}

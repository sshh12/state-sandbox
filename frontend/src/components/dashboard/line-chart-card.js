import {
  Line,
  LineChart as RechartsLineChart,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
} from 'recharts';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { getValue, formatNumber, formatMonthDate } from '@/lib/utils';

export default function LineChartCard({
  title,
  snapshots,
  valueKey,
  span = 3,
}) {
  const chartData = [...snapshots]
    .sort((a, b) => new Date(a.date) - new Date(b.date))
    .map((snap) => ({
      name: formatMonthDate(snap.date),
      total: getValue(snap, valueKey).value,
    }));

  return (
    <Card className={`col-span-${span}`}>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
      </CardHeader>
      <CardContent className="pl-2">
        <ResponsiveContainer width="100%" height={350}>
          <RechartsLineChart data={chartData}>
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
              domain={[
                (dataMin) => dataMin * 0.95,
                (dataMax) => dataMax * 1.05,
              ]}
              allowDataOverflow={true}
              tickFormatter={formatNumber}
            />
            <Tooltip
              contentStyle={{
                backgroundColor: 'white',
                border: '1px solid #ccc',
                borderRadius: '4px',
                padding: '8px',
              }}
              formatter={(value) => [`${value}`]}
            />
            <Line
              type="monotone"
              dataKey="total"
              stroke="#000000"
              strokeWidth={2}
              dot={false}
              className="stroke-primary"
            />
          </RechartsLineChart>
        </ResponsiveContainer>
      </CardContent>
    </Card>
  );
}

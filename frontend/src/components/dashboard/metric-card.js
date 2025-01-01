import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { formatValue, formatDiff } from '@/lib/utils';

export default function MetricCard({ snapshots, title, valueKey, icon }) {
  const Icon = icon;
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        <Icon className="h-4 w-4 text-muted-foreground" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">
          {formatValue(snapshots[0], valueKey)}
        </div>
        <p className="text-xs text-muted-foreground">
          {formatDiff(snapshots[1], snapshots[0], valueKey)} from last month
        </p>
      </CardContent>
    </Card>
  );
}

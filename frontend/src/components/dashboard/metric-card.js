import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { formatValue, formatDiff } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import { LineChart } from 'lucide-react';
import { useState } from 'react';
import { MetricLineChartDialog } from './metric-line-chart-dialog';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';

export default function MetricCard({ snapshots, title, valueKey, icon: Icon }) {
  const [showChart, setShowChart] = useState(false);

  return (
    <>
      <Card className="group">
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-sm font-medium">{title}</CardTitle>
          <div className="flex items-center gap-2">
            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 transition-colors hover:bg-primary hover:text-primary-foreground"
                    onClick={() => setShowChart(true)}
                  >
                    <LineChart className="h-4 w-4" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent>
                  <p>View trend over time</p>
                </TooltipContent>
              </Tooltip>
            </TooltipProvider>
            {Icon && <Icon className="h-4 w-4 text-muted-foreground" />}
          </div>
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
      <MetricLineChartDialog
        isOpen={showChart}
        onOpenChange={setShowChart}
        title={title}
        snapshots={snapshots}
        valueKey={valueKey}
      />
    </>
  );
}

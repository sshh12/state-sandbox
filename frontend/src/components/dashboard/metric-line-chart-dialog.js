import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import LineChartCard from './line-chart-card';

export function MetricLineChartDialog({
  isOpen,
  onOpenChange,
  title,
  snapshots,
  valueKey,
}) {
  if (!snapshots?.length) return null;

  return (
    <Dialog open={isOpen} onOpenChange={onOpenChange}>
      <DialogContent className="max-w-[95vw] sm:max-w-[800px]">
        <DialogHeader>
          <DialogTitle>{title} Over Time</DialogTitle>
        </DialogHeader>
        <div className="pt-4">
          <LineChartCard
            title=""
            snapshots={snapshots}
            valueKey={valueKey}
            span={6}
          />
        </div>
      </DialogContent>
    </Dialog>
  );
}

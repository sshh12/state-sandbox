import { useEffect, useState } from 'react';
import { Progress } from '@/components/ui/progress';

export function ProgressTimer({
  duration = 5 * 60 * 1000, // default 5 minutes
  isRunning = false,
  className,
  showPercentage = true,
}) {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    if (isRunning) {
      setProgress(0);
      const interval = 100; // Update every 100ms
      const step = (interval / duration) * 100;

      const timer = setInterval(() => {
        setProgress((prev) => {
          const next = prev + step;
          return next > 100 ? 100 : next;
        });
      }, interval);

      return () => clearInterval(timer);
    } else {
      setProgress(0);
    }
  }, [isRunning, duration]);

  return (
    <div className="space-y-2">
      <Progress value={progress} className={className} />
      {showPercentage && (
        <p className="text-sm text-muted-foreground text-center">
          {Math.round(progress)}%
        </p>
      )}
    </div>
  );
}

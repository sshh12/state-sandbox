import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';
import { HelpCircle } from 'lucide-react';
import { Button } from '@/components/ui/button';

export function HelpDialog({ state, open, onOpenChange }) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogTrigger asChild>
        <Button variant="ghost" className="gap-2">
          <HelpCircle className="h-5 w-5" />
          Help
        </Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>How to Play</DialogTitle>
          <DialogDescription>
            <div className="space-y-4">
              {state?.name && (
                <div className="space-y-4 pt-4">
                  <p>
                    You are the leader of {state.name} and are tasked with
                    running the country. Click "play" to see the upcoming
                    challenges your nation will face over the next year and
                    define arbitrary policy decisions to handle them. Explore
                    the dashboard to learn about {state.name} and how to act
                    effectively.
                  </p>
                  <p>
                    Policies should handle upcoming events (suggested policies
                    are also included) but you can also pass other laws to see
                    how they will play out. Compete on the leaderboard by
                    enacting policies that optimize for GDP, population, and
                    other metrics.
                  </p>
                </div>
              )}
              {state?.description && (
                <div className="space-y-4 pt-4 bg-muted rounded-lg p-4">
                  <p>{state.description}</p>
                </div>
              )}
            </div>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}

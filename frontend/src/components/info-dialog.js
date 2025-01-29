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

export function InfoDialog({
  title,
  state,
  open,
  onOpenChange,
  includeInstructions,
}) {
  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogTrigger asChild>
        <Button variant="ghost" className="gap-2">
          <HelpCircle className="h-5 w-5" />
          Help
        </Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[600px] max-h-[80vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>{title}</DialogTitle>
          <DialogDescription>
            Learn more about your state and how to play the game effectively.
          </DialogDescription>
        </DialogHeader>
        <div className="grid gap-4 py-4">
          {includeInstructions && state?.name && (
            <div className="space-y-4">
              <DialogDescription>
                You are the leader of <strong>{state.name}</strong> and are
                tasked with running the country. Click "play" to see the
                upcoming challenges your nation will face over the next year and
                define arbitrary policy decisions to handle them. Explore the
                dashboard to learn about <strong>{state.name}</strong> and how
                to act effectively.
              </DialogDescription>
              <DialogDescription>
                Policies should handle upcoming events (suggested policies are
                also included) but you can also pass other laws to see how they
                will play out. Compete on the leaderboard by enacting policies
                that optimize for GDP, population, and other metrics.
              </DialogDescription>
            </div>
          )}
          {state?.description && (
            <div className="bg-muted rounded-lg p-4">
              <DialogDescription>{state.description}</DialogDescription>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}

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

export function HelpDialog() {
  return (
    <Dialog>
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
            <div className="space-y-4 pt-4">
              <p>Here's how to interact with the simulation:</p>
              <ul className="list-disc pl-4 space-y-2">
                <li>Click Play to start the simulation</li>
                <li>Use the controls to adjust simulation speed</li>
                <li>
                  View different aspects of your state using the tabs below
                </li>
              </ul>
            </div>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}

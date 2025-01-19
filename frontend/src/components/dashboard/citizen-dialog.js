import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Badge } from '@/components/ui/badge';

export default function CitizenDialog({ isOpen, onClose, citizen }) {
  const { name, age, gender, race, religion, occupation, income, biography } =
    citizen;

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>{name}</DialogTitle>
        </DialogHeader>
        <ScrollArea className="max-h-[60vh]">
          <div className="space-y-6">
            <div className="flex flex-wrap gap-2">
              <Badge variant="outline">{age}</Badge>
              <Badge variant="outline">{gender}</Badge>
              <Badge variant="outline">{race}</Badge>
              <Badge variant="outline">{religion}</Badge>
            </div>
            <div className="flex gap-2 text-sm text-muted-foreground">
              <span>{occupation}</span>
              <span>•</span>
              <span>{income}</span>
            </div>
            <div className="space-y-4">
              <p className="text-sm leading-relaxed whitespace-pre-wrap">
                {biography || 'Biography not yet available.'}
              </p>
            </div>
          </div>
        </ScrollArea>
      </DialogContent>
    </Dialog>
  );
}

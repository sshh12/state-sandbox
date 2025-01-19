import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { ScrollArea } from '@/components/ui/scroll-area';

export default function HeadlineDialog({
  isOpen,
  onClose,
  headline,
  fullStory,
}) {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl">
        <DialogHeader>
          <DialogTitle>{headline}</DialogTitle>
        </DialogHeader>
        <ScrollArea className="max-h-[60vh]">
          <div className="space-y-4">
            <p className="text-sm leading-relaxed whitespace-pre-wrap">
              {fullStory || 'Full story not yet available.'}
            </p>
          </div>
        </ScrollArea>
      </DialogContent>
    </Dialog>
  );
}

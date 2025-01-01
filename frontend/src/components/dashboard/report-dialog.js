'use client';

import ReactMarkdown from 'react-markdown';
import { Dialog, DialogContent, DialogTitle } from '@/components/ui/dialog';

export function ReportDialog({ isOpen, onOpenChange, report }) {
  if (!report) return null;

  return (
    <Dialog
      open={isOpen}
      onOpenChange={(open, event) => {
        if (event?.type === 'pointerDownOutside') {
          event.preventDefault();
          return;
        }
        onOpenChange(open);
      }}
    >
      <DialogContent className="max-w-[95vw] md:max-w-3xl lg:max-w-4xl max-h-[80vh] overflow-y-auto">
        <DialogTitle className="sr-only">Report</DialogTitle>
        <div className="prose prose-sm dark:prose-invert">
          <ReactMarkdown>{report}</ReactMarkdown>
        </div>
      </DialogContent>
    </Dialog>
  );
}

'use client';

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import Image from 'next/image';

export function WhatIsThisModal({ isOpen, onClose }) {
  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>About State Sandbox</DialogTitle>
          <DialogDescription className="space-y-4 pt-4">
            <p>
              State Sandbox is an experimental game for socioeconomic
              simulation, powered by Large Language Models (o3-mini) to simulate
              complex policy impacts on a virtual society.
            </p>
            <p>
              As a leader, you'll navigate high-dimensional gameplay across
              multiple domains: people, economy, media, crime, environment, and
              more. Make arbitrary policy decisions, respond to realistic random
              events and natural disasters, and see how your choices shape your
              nation's future.
            </p>
            <div className="relative w-full h-[300px] my-4">
              <Image
                src="/demo.png"
                alt="State Sandbox Demo"
                fill
                className="object-contain"
                priority
              />
            </div>
            <p>
              Compete on the leaderboard by optimizing your nation's GDP,
              population, and other key metrics. This is an experimental
              research project - data may be reset without notice. Try it out
              with a temporary account or create a permanent one to track your
              progress.
            </p>
          </DialogDescription>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}

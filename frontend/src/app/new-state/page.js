'use client';

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { cn } from '@/lib/utils';
import { useState, useMemo, useEffect } from 'react';
import { api } from '@/lib/api';
import { useRouter } from 'next/navigation';

const questions = [
  'The government should prioritize economic growth over environmental protection',
  'Healthcare should be provided by the government for all citizens',
  'Education should be free at all levels',
  'Military spending should be increased',
  'Immigration policies should be more strict',
  'The tax system should be more progressive',
  'Public transportation should be prioritized over private vehicles',
  'The government should regulate big tech companies more strictly',
  'Renewable energy should be subsidized',
  'Social welfare programs should be expanded',
];

const ratingOptions = [
  {
    value: '1',
    label: 'Strongly Disagree',
    color: 'bg-red-700 hover:bg-red-800',
  },
  { value: '2', label: 'Disagree', color: 'bg-red-500 hover:bg-red-600' },
  { value: '3', label: 'Neutral', color: 'bg-gray-500 hover:bg-gray-600' },
  { value: '4', label: 'Agree', color: 'bg-green-500 hover:bg-green-600' },
  {
    value: '5',
    label: 'Strongly Agree',
    color: 'bg-green-700 hover:bg-green-800',
  },
];

const loadingMessages = [
  'Designing the flag...',
  'Recruiting an army...',
  'Establishing government...',
  'Writing the constitution...',
  'Building infrastructure...',
  'Training diplomats...',
  'Setting up the economy...',
  'Founding the capital city...',
  'Minting currency...',
  'Creating national parks...',
  'Composing national anthem...',
  'Establishing time zones...',
  'Drawing border lines...',
  'Setting up postal service...',
  'Designing official seals...',
  'Planting national tree...',
  'Choosing national bird...',
  'Building parliament...',
  'Training civil servants...',
  'Establishing courts...',
];

export default function NewState() {
  const [ratings, setRatings] = useState({});
  const [countryName, setCountryName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [loadingMessageIndex, setLoadingMessageIndex] = useState(0);
  const router = useRouter();

  const isFormValid = useMemo(() => {
    return (
      countryName.trim() !== '' &&
      Object.keys(ratings).length === questions.length
    );
  }, [countryName, ratings]);

  useEffect(() => {
    let interval;
    if (isLoading) {
      interval = setInterval(() => {
        setLoadingMessageIndex((prev) => (prev + 1) % loadingMessages.length);
      }, 3000); // Change message every 2 seconds
    }
    return () => clearInterval(interval);
  }, [isLoading]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!isFormValid) return;

    setIsLoading(true);
    try {
      const questionData = questions.map((question, index) => ({
        question,
        value: parseInt(ratings[index]),
      }));

      const state = await api.createState(countryName, questionData);
      router.push(`/state/${state.id}`);
    } catch (error) {
      console.error('Failed to create state:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRatingClick = (questionIndex, value) => {
    setRatings((prev) => ({
      ...prev,
      [questionIndex]: value,
    }));
  };

  return (
    <div className="min-h-screen flex">
      {/* Left Panel with Form */}
      <div className="flex-1 p-6 md:p-10">
        <div className="max-w-[800px] mx-auto">
          <h1 className="text-2xl font-semibold mb-2">Create a new Country</h1>
          <p className="text-muted-foreground mb-4">
            Fill out the fields below to create a new country. Your choices will
            influence the country's policies, structure, and more.
          </p>
          <p className="text-sm text-muted-foreground mb-8 italic">
            Disclaimer: States Sandbox is a Large Language Model-based
            simulation and does not reflect real-world governance. The outcomes
            are influenced by the biases present in our prompts and underlying
            AI models, and should not be taken as realistic predictions. The
            game and many of it's characteristics are inspired by{' '}
            <a href="https://nationstates.net">NationStates</a>.
          </p>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="space-y-3">
              <Label htmlFor="country">Country Name</Label>
              <Input
                id="country"
                placeholder="Enter suggested country name"
                className="w-full"
                value={countryName}
                onChange={(e) => setCountryName(e.target.value)}
                required
              />
            </div>

            {questions.map((question, index) => (
              <div key={index} className="space-y-3">
                <Label className="block text-base">{question}</Label>
                <div className="grid grid-cols-5 gap-2">
                  {ratingOptions.map((option) => (
                    <Button
                      key={option.value}
                      type="button"
                      variant={
                        ratings[index] === option.value ? 'default' : 'outline'
                      }
                      className={cn(
                        'px-2 h-11 whitespace-nowrap',
                        ratings[index] === option.value
                          ? cn(option.color, 'text-white border-0')
                          : 'hover:bg-gray-100'
                      )}
                      onClick={() => handleRatingClick(index, option.value)}
                    >
                      {option.label}
                    </Button>
                  ))}
                </div>
              </div>
            ))}

            <Button
              type="submit"
              className={cn(
                'w-full h-11 mt-8',
                !isFormValid && 'opacity-50 cursor-not-allowed'
              )}
              disabled={!isFormValid || isLoading}
            >
              {isLoading ? loadingMessages[loadingMessageIndex] : 'Create'}
            </Button>
          </form>
        </div>
      </div>

      {/* Right Panel */}
      <div className="hidden md:block flex-1 bg-black" />
    </div>
  );
}

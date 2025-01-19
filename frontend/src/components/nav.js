'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { useUser } from '@/context/user-context';
import { FlagSVG } from '@/components/flag-svg';
import { Menu, Plus } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Sheet, SheetContent, SheetTrigger } from '@/components/ui/sheet';

const links = [
  { name: 'Leaderboard', href: '/leaderboard' },
  { name: 'Account', href: '/account' },
  {
    name: 'Feedback',
    href: 'https://forms.gle/KDbeBvVLnj2sNaHeA',
    target: '_blank',
    rel: 'noopener noreferrer',
  },
];

export function DashboardNav({ stateId }) {
  const pathname = usePathname();
  const { states } = useUser();
  const idInStates = states?.find((state) => state.id === stateId);

  const NavLinks = () => (
    <>
      {links.map((link) => (
        <Link
          key={link.href}
          href={link.href}
          target={link.target}
          rel={link.rel}
          className={`py-4 text-sm font-medium transition-colors hover:text-primary ${
            pathname === link.href ? 'text-foreground' : 'text-muted-foreground'
          }`}
        >
          {link.name}
        </Link>
      ))}
    </>
  );

  const StateSelector = () => (
    <div className="flex items-center gap-2">
      <Select
        value={idInStates?.id || ''}
        onValueChange={(value) => (window.location.href = `/state/${value}`)}
      >
        <SelectTrigger className="w-[180px]">
          <SelectValue defaultValue="" placeholder="Select Nation" />
        </SelectTrigger>
        <SelectContent>
          {(states || []).map((state) => (
            <SelectItem key={state.id} value={'' + state.id}>
              <div className="flex items-center gap-2">
                <FlagSVG svgString={state.flag_svg} />
                {state.name}
              </div>
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
      <Button variant="outline" size="icon" asChild>
        <Link href="/new-state">
          <Plus className="h-4 w-4" />
          <span className="sr-only">Add new state</span>
        </Link>
      </Button>
    </div>
  );

  return (
    <nav className="flex items-center justify-between border-b px-6 py-2">
      <div className="flex flex-1 items-center space-x-3">
        <StateSelector />
      </div>

      {/* Desktop Navigation */}
      <div className="hidden md:flex items-center space-x-8">
        <NavLinks />
      </div>

      {/* Mobile Navigation */}
      <div className="md:hidden">
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon">
              <Menu className="h-5 w-5" />
              <span className="sr-only">Toggle menu</span>
            </Button>
          </SheetTrigger>
          <SheetContent side="right">
            <div className="flex flex-col space-y-4 mt-8">
              <NavLinks />
            </div>
          </SheetContent>
        </Sheet>
      </div>
    </nav>
  );
}

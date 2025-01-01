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

const links = [
  { name: 'States', href: '/states' },
  { name: 'Leaderboard', href: '/leaderboard' },
  { name: 'Profile', href: '/profile' },
];

export function DashboardNav({ stateId }) {
  const pathname = usePathname();
  const { states } = useUser();

  return (
    <nav className="flex items-center space-x-8 border-b px-6">
      <div className="flex items-center space-x-3">
        <Select
          value={'' + stateId}
          onValueChange={(value) => (window.location.href = `/state/${value}`)}
        >
          <SelectTrigger className="w-[200px] bg-background border border-input hover:bg-accent hover:text-accent-foreground">
            <SelectValue placeholder="Select state" />
          </SelectTrigger>
          <SelectContent>
            {(states || []).map((state) => (
              <SelectItem key={state.id} value={'' + state.id}>
                {state.name}
              </SelectItem>
            ))}
          </SelectContent>
        </Select>
      </div>

      {links.map((link) => (
        <Link
          key={link.href}
          href={link.href}
          className={`py-4 text-sm font-medium transition-colors hover:text-primary ${
            pathname === link.href ? 'text-foreground' : 'text-muted-foreground'
          }`}
        >
          {link.name}
        </Link>
      ))}
    </nav>
  );
}

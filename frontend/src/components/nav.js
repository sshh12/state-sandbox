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

const links = [
  { name: 'States', href: '/states' },
  { name: 'Leaderboard', href: '/leaderboard' },
  { name: 'Profile', href: '/profile' },
];

export function DashboardNav() {
  const pathname = usePathname();

  return (
    <nav className="flex items-center space-x-8 border-b px-6">
      <div className="flex items-center space-x-3">
        <div className="w-8 h-8 bg-gray-200 rounded-full" />
        <Select defaultValue="alicia">
          <SelectTrigger className="w-[140px] border-0 focus:ring-0">
            <SelectValue placeholder="Select user" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="alicia">Alicia Koch</SelectItem>
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

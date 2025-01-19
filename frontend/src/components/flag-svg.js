import { ReactSVG } from 'react-svg';
import {
  Dialog,
  DialogContent,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';

export function FlagSVG({
  svgString,
  className,
  size = '1rem',
  allowExpand = false,
}) {
  if (!svgString) return null;

  // Extract width and height from SVG string if they exist
  const widthMatch = svgString.match(/width="(\d+)"/);
  const heightMatch = svgString.match(/height="(\d+)"/);
  const width = widthMatch ? parseInt(widthMatch[1]) : 24;
  const height = heightMatch ? parseInt(heightMatch[1]) : 24;

  // Add or replace viewBox while preserving other attributes and formatting
  const modifiedSvgString = svgString.replace(/(<svg[^>]*)>/, (match, p1) => {
    // Remove existing viewBox if present
    const cleanedAttributes = p1.replace(/viewBox="[^"]*"/, '');
    return `${cleanedAttributes} viewBox="0 0 ${width} ${height}">`;
  });

  const svgBlob = new Blob([modifiedSvgString], { type: 'image/svg+xml' });
  const url = URL.createObjectURL(svgBlob);

  const SvgComponent = (
    <ReactSVG
      src={url}
      wrapper="span"
      className={className}
      onLoad={() => URL.revokeObjectURL(url)}
      beforeInjection={(svg) => {
        svg.removeAttribute('width');
        svg.removeAttribute('height');
        svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
        svg.style.height = size;
        svg.style.width = 'auto';
        svg.style.display = 'inline-block';
        svg.style.verticalAlign = 'middle';
      }}
    />
  );

  if (!allowExpand) {
    return SvgComponent;
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <div className="cursor-pointer">{SvgComponent}</div>
      </DialogTrigger>
      <DialogContent className="max-w-[90vw] max-h-[90vh]">
        <DialogTitle className="mb-4">Flag Preview</DialogTitle>
        <ReactSVG
          src={url}
          wrapper="span"
          className="w-full h-full"
          onLoad={() => URL.revokeObjectURL(url)}
          beforeInjection={(svg) => {
            svg.removeAttribute('width');
            svg.removeAttribute('height');
            svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
            svg.style.maxWidth = '100%';
            svg.style.width = 'auto';
            svg.style.maxHeight = '80vh';
            svg.style.height = 'auto';
            svg.style.display = 'block';
            svg.style.margin = 'auto';
          }}
        />
      </DialogContent>
    </Dialog>
  );
}

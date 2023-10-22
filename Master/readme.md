What is this?

A collection of master files for icon development.
- There should be one (or more) files per workbench.
- If a workbench deserves more files, we should group by funcions and use sensible file names (es. Sketcher-Constraints, Sketcher-Geometry).
- Since the output file(s) name(s) are dictated by the page named defined inside the inkscape files, we are not forced with the master file names and we can add info on the filename itself.
- Since the batch export only cares of things that are in a page, we can keep notes, working copies, whatever inside the files, as long as they are outside the page(s) area. 

The files are meant to produce the single icon file automatically using Inkscape's batch export function. The page name dictates the name of the sigle file.

Where should we go next? (next days)
- complete the Mesh, Spreadsheet, Surface and Dynamic data master files (let's make sure we have all required pages and the export process works)
- double check all symbols against the Material Design(ish) size mask
- PR to Obelisc79 with the single icon outputs 

Where should we go then?
- shuld we aggregate existing Obelis work back into master files? It will make life easier for maintenance (adding new functions, whatever)
- it is a freaking big task on it's own, maybe is worth investigating some kind of automation (they are xml files, so it should be possible to glue them together with Pytnon)

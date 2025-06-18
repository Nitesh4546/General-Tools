extn = {
    # General Purpose Languages
    'py': 'Python Script',
    'pyc': 'Compiled Python File',
    'pyo': 'Optimized Python File',
    'ipynb': 'Jupyter Notebook',
    'c': 'C Source File',
    'h': 'C/C++ Header File',
    'cpp': 'C++ Source File',
    'cc': 'C++ Source File',
    'cxx': 'C++ Source File',
    'c++': 'C++ Source File',
    'hpp': 'C++ Header File',
    'cs': 'C# Source File',
    'java': 'Java Source File',
    'class': 'Compiled Java Class File',
    'kt': 'Kotlin Source File',
    'kts': 'Kotlin Script',
    'rs': 'Rust Source File',
    'go': 'Go Source File',
    'swift': 'Swift Source File',
    'm': 'Objective-C Source File',
    'mm': 'Objective-C++ Source File',
    'scala': 'Scala Source File',
    'sh': 'Shell Script',
    'bash': 'Bash Script',
    'zsh': 'Zsh Script',
    'bat': 'Batch File',
    'ps1': 'PowerShell Script',
    'rb': 'Ruby Script',
    'pl': 'Perl Script',
    'pm': 'Perl Module',
    'lua': 'Lua Script',
    'r': 'R Script',
    'jl': 'Julia Source File',
    'ts': 'TypeScript File',
    'tsx': 'TypeScript + JSX File',
    'jsx': 'JavaScript + JSX File',
    'dart': 'Dart Source File',

    # Web-related
    'html': 'HTML Document',
    'htm': 'HTML Document',
    'xhtml': 'XHTML Document',
    'xml': 'XML File',
    'css': 'CSS Stylesheet',
    'scss': 'Sass Stylesheet',
    'sass': 'Sass Stylesheet',
    'less': 'LESS Stylesheet',
    'js': 'JavaScript File',
    'json': 'JSON File',
    'yaml': 'YAML File',
    'yml': 'YAML File',

    # Configuration/Markup
    'ini': 'INI Configuration File',
    'cfg': 'Configuration File',
    'toml': 'TOML File',
    'env': 'Environment Variables File',
    'conf': 'Configuration File',
    'md': 'Markdown Document',
    'rst': 'reStructuredText Document',
    'tex': 'LaTeX Source File',

    # Data & Serialization
    'csv': 'CSV File',
    'tsv': 'TSV File',
    'db': 'Database File',
    'db3': 'SQLite Database File',
    'sqlite': 'SQLite Database File',
    'pkl': 'Pickle File',
    'h5': 'HDF5 File',
    'parquet': 'Parquet File',
    'avro': 'Avro Data File',

    # Miscellaneous
    'makefile': 'Makefile',
    'mk': 'Makefile',
    'cmake': 'CMake File',
    'dockerfile': 'Dockerfile',
    'gradle': 'Gradle Build Script',
    'pom': 'Maven POM File',
    'build': 'Build File',
    'asm': 'Assembly Source File',
    's': 'Assembly Source File',

    # Bytecode / Executable / Object
    'o': 'Object File',
    'obj': 'Object File',
    'dll': 'Dynamic Link Library',
    'so': 'Shared Object File',
    'a': 'Static Library File',
    'lib': 'Static Library File',
    'exe': 'Windows Executable',
    'out': 'Compiled Binary File',
    'class': 'Java Bytecode File',
    'jar': 'Java Archive File',
    'war': 'Web Application Archive',
    'apk': 'Android Package',
    'ipa': 'iOS Application Archive',

    # Script runners / Interpreters
    'php': 'PHP Script',
    'asp': 'ASP Script',
    'aspx': 'ASP.NET Page',
    'cgi': 'Common Gateway Interface Script',

    # Others
    'sql': 'SQL Script',
    'vb': 'Visual Basic File',
    'vbs': 'VBScript File',
    'erl': 'Erlang Source File',
    'ex': 'Elixir Source File',
    'exs': 'Elixir Script File',
    'clj': 'Clojure Source File',
    'cljs': 'ClojureScript File',
    'groovy': 'Groovy Script',
    'nasm': 'Netwide Assembler File'
}

doc = [
    # Plain Text & Rich Text
    'txt',     # Plain text
    'rtf',     # Rich Text Format
    'md',      # Markdown
    'rst',     # reStructuredText

    # Word Processing Documents
    'doc',     # Microsoft Word (legacy)
    'docx',    # Microsoft Word (OpenXML)
    'odt',     # OpenDocument Text (LibreOffice/OpenOffice)
    'pages',   # Apple Pages

    # Spreadsheets
    'xls',     # Microsoft Excel (legacy)
    'xlsx',    # Microsoft Excel (OpenXML)
    'ods',     # OpenDocument Spreadsheet
    'csv',     # Comma-Separated Values
    'tsv',     # Tab-Separated Values

    # Presentations
    'ppt',     # Microsoft PowerPoint (legacy)
    'pptx',    # Microsoft PowerPoint (OpenXML)
    'odp',     # OpenDocument Presentation
    'key',     # Apple Keynote

    # PDF & eBooks
    'pdf',     # Portable Document Format
    'epub',    # EPUB eBook
    'mobi',    # Mobipocket eBook
    'azw',     # Amazon Kindle eBook
    'fb2',     # FictionBook eBook

    # Markup & Web Docs
    'html',    # HTML Document
    'htm',     # HTML Document
    'xml',     # XML File
    'xhtml',   # XHTML Document
    'tex',     # LaTeX Source File

    # Notes & Outlines
    'one',     # Microsoft OneNote
    'nb',      # Mathematica Notebook
    'gdoc',    # Google Docs (shortcut)
    'gsheet',  # Google Sheets (shortcut)
    'gslides'  # Google Slides (shortcut)
]

pic = [
    # Raster image formats
    'jpg',     # JPEG image
    'jpeg',    # JPEG image
    'png',     # Portable Network Graphics
    'gif',     # Graphics Interchange Format
    'bmp',     # Bitmap image
    'tif',     # Tagged Image File Format
    'tiff',    # Tagged Image File Format
    'webp',    # Web Picture format
    'ico',     # Icon file
    'heic',    # High Efficiency Image Coding (Apple)
    'heif',    # High Efficiency Image Format

    # Vector image formats
    'svg',     # Scalable Vector Graphics
    'eps',     # Encapsulated PostScript
    'ai',      # Adobe Illustrator File
    'cdr',     # CorelDRAW File

    # Raw image formats (from cameras)
    'raw',     # Generic raw image
    'arw',     # Sony RAW
    'cr2',     # Canon RAW 2
    'crw',     # Canon RAW
    'nef',     # Nikon Electronic Format
    'orf',     # Olympus RAW Format
    'rw2',     # Panasonic RAW Format
    'dng',     # Digital Negative

    # Others
    'apng',    # Animated PNG
    'psd',     # Adobe Photoshop Document
    'xcf',      # GIMP Image File
    'webp'    # WebP Image
]

audi = [
    'mp3',     # MPEG Layer 3 Audio
    'wav',     # Waveform Audio File
    'flac',    # Free Lossless Audio Codec
    'aac',     # Advanced Audio Coding
    'ogg',     # Ogg Vorbis Audio
    'wma',     # Windows Media Audio
    'm4a',     # MPEG-4 Audio
    'alac',    # Apple Lossless Audio Codec
    'opus',    # Opus Audio Codec
    'amr',     # Adaptive Multi-Rate
    'aiff',    # Audio Interchange File Format
    'au',      # AU Audio File
    'ra',      # RealAudio
    'voc'      # Creative Voice File
]

video = [
    'mp4',     # MPEG-4 Video
    'mkv',     # Matroska Video File
    'avi',     # Audio Video Interleave
    'mov',     # Apple QuickTime Movie
    'flv',     # Flash Video
    'wmv',     # Windows Media Video
    'webm',    # WebM Video
    '3gp',     # 3GPP Multimedia File
    'mpg',     # MPEG Video
    'mpeg',    # MPEG Video
    'm4v',     # MPEG-4 Video File
    'ts',      # MPEG Transport Stream
    'vob',     # DVD Video Object
    'rm',      # RealMedia
    'ogv'      # Ogg Video
]

archive = [
    'zip',     # ZIP Archive
    'rar',     # RAR Archive
    '7z',      # 7-Zip Archive
    'tar',     # Tape Archive
    'gz',      # Gzip Compressed File
    'bz2',     # Bzip2 Compressed File
    'xz',      # XZ Compressed Archive
    'tgz',     # Tarball Gzip
    'tar.gz',  # Tarball Gzip
    'tar.bz2', # Tarball Bzip2
    'tar.xz',  # Tarball XZ
    'lz',      # Lzip Compressed File
    'lzma',    # LZMA Compressed File
    'z',       # Unix Compress File
    'iso',     # Disk Image
    'dmg',     # Apple Disk Image
    'cab',     # Windows Cabinet File
    'arj',     # ARJ Compressed Archive
    'deb',     # Debian Package
    'rpm',     # Red Hat Package Manager File
    'apk',     # Android Package
    'jar',     # Java Archive
    'war'      # Web Application Archive
]

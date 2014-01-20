# Generated automatically from Makefile.PL.in by configure.
use ExtUtils::MakeMaker;
# See lib/ExtUtils/MakeMaker.pm for details of how to influence
# the contents of the Makefile that is written.
WriteMakefile(
    'CC'		=> 'c++',
    'NAME'		=> 'TinySVM',
    'INC'		=> '-I/home/ywangby/data/workspace/tweets_conceptualization/src/twitter_nlp/TinySVM-0.09/..//include',
    'LIBS'        	=> '-L/home/ywangby/data/workspace/tweets_conceptualization/src/twitter_nlp/TinySVM-0.09/..//lib -ltinysvm',
    'OBJECT'            => 'TinySVM_wrap.o'
);

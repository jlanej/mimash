package main

import (
	"compress/gzip"
	"fmt"
	"github.com/brentp/vcfgo"
	"io"
	"os"
	"strings"
)

// get reader for vcf file
// return a io.Reader for the vcf file
func getreader(vcfFile string) io.Reader {
	f, err := os.Open(vcfFile)
	if err != nil {
		panic(err)
	}

	if strings.HasSuffix(vcfFile, ".gz") {
		gz, err := gzip.NewReader(f)
		if err != nil {
			panic(err)
		}
		return gz
	} else {
		return f
	}
}

//parses a vcf file with multiple samples
//creates a consensus sequence for a list of samples in the vcf
//returns the consensus sequence

func parseVcfSamples(vcfFile string) {

	fmt.Println("Parsing vcf file: ", vcfFile)
	f := getreader(vcfFile)

	rdr, err := vcfgo.NewReader(f, false)
	if err != nil {
		panic(err)
	}
	for {
		variant := rdr.Read()
		if variant == nil {
			break
		}
		fmt.Printf("%s\t%d\t%s\t%s\n", variant.Chromosome, variant.Pos, variant.Ref, variant.Alt)
	}
}

func main() {
	vcfFile := "data/1000G/ALL.chrMT.phase3_callmom-v0_4.20130502.genotypes.vcf.gz"
	parseVcfSamples(vcfFile)
}

import sst
from mhlib import componentlist

# Global variables
debugScratch = 0
debugL1 = 0
debugL2 = 0
core_clock = "2GHz"

# Define the simulation components
comp_cpu0 = sst.Component("cpu0", "memHierarchy.ScratchCPU")
iface0 = comp_cpu0.setSubComponent("memory", "memHierarchy.scratchInterface")
iface0.addParams({ "scratchpad_size" : "64KiB" })
comp_cpu0.addParams({
    "scratchSize" : 65536,   # 64K scratch
    "maxAddr" : 2097152,       # 2M mem
    "scratchLineSize" : 64,
    "memLineSize" : 128,
    "clock" : core_clock,
    "maxOutstandingRequests" : 16,
    "maxRequestsPerCycle" : 2,
    "reqsToIssue" : 1000,
    "verbose" : 1,
    "rngseed" : 111
})

comp_l1_0 = sst.Component("l1_0", "memHierarchy.Cache")
comp_l1_0.addParams({
    "debug" : debugL1,
    "debug_level" : 10,
    "cache_frequency" : core_clock,
    "cache_size" : "4KiB",
    "access_latency_cycles" : 1,
    "coherence_protocol" : "MESI",
    "cache_line_size" : 64,
    "L1" : 1,
    "associativity" : 4,
    "replacement_policy" : "lru",
})
comp_l2_0 = sst.Component("l2_0", "memHierarchy.Cache")
comp_l2_0.addParams({
    "debug" : debugL2,
    "debug_level" : 10,
    "cache_frequency" : core_clock,
    "cache_size" : "16KiB",
    "access_latency_cycles" : 5,
    "cache_type" : "noninclusive",
    "coherence_protocol" : "MESI",
    "cache_line_size" : 64,
    "associativity" : 8,
    "replacement_policy" : "mru",
})

comp_scratch0 = sst.Component("scratch0", "memHierarchy.Scratchpad")
comp_scratch0.addParams({
    "debug" : debugScratch,
    "debug_level" : 5,
    "clock" : core_clock,
    "size" : "64KiB",
    "scratch_line_size" : 64,
    "memory_line_size" : 128,
    "backing" : "none",
    "backendConvertor" : "memHierarchy.simpleMemScratchBackendConvertor",
    "backendConvertor.backend" : "memHierarchy.simpleMem",
    "backendConvertor.backend.access_time" : "10ns",
    "memNIC.network_bw" : "50GB/s",
})
comp_cpu1 = sst.Component("cpu1", "memHierarchy.ScratchCPU")
iface1 = comp_cpu1.setSubComponent("memory", "memHierarchy.scratchInterface")
iface1.addParams({ "scratchpad_size" : "64KiB" })
comp_cpu1.addParams({
    "scratchSize" : 65536,   # 64K scratch
    "maxAddr" : 2097152,       # 2M mem
    "scratchLineSize" : 64,
    "memLineSize" : 128,
    "clock" : core_clock,
    "maxOutstandingRequests" : 16,
    "maxRequestsPerCycle" : 2,
    "reqsToIssue" : 1000,
    "verbose" : 1,
    "rngseed" : 90
})
comp_l1_1 = sst.Component("l1_1", "memHierarchy.Cache")
comp_l1_1.addParams({
    #"debug" : debugL1,
    "debug_level" : 3,
    "cache_frequency" : core_clock,
    "cache_size" : "4KiB",
    "access_latency_cycles" : 4,
    "coherence_protocol" : "MESI",
    "cache_line_size" : 64,
    "L1" : 1,
    "associativity" : 4,
    "replacement_policy" : "lru",
})
comp_l2_1 = sst.Component("l2_1", "memHierarchy.Cache")
comp_l2_1.addParams({
    "debug" : debugL2,
    "debug_level" : 10,
    "cache_frequency" : core_clock,
    "cache_size" : "16KiB",
    "access_latency_cycles" : 5,
    "cache_type" : "noninclusive",
    "coherence_protocol" : "MESI",
    "cache_line_size" : 64,
    "associativity" : 8,
    "replacement_policy" : "mru",
})
comp_scratch1 = sst.Component("scratch1", "memHierarchy.Scratchpad")
comp_scratch1.addParams({
    #"debug" : debugScratch,
    "debug_level" : 5,
    "clock" : core_clock,
    "size" : "64KiB",
    "scratch_line_size" : 64,
    "memory_line_size" : 128,
    "backing" : "none",
    "backendConvertor" : "memHierarchy.simpleMemScratchBackendConvertor",
    "backendConvertor.backend" : "memHierarchy.simpleMem",
    "backendConvertor.backend.access_time" : "10ns",
    "memNIC.network_bw" : "50GB/s",
})
comp_net = sst.Component("network", "merlin.hr_router")
comp_net.addParams({
    "xbar_bw" : "50GB/s",
    "link_bw" : "50GB/s",
    "input_buf_size" : "1KiB",
    "output_buf_size" : "1KiB",
    "flit_size" : "72B",
    "id" : "0",
    "topology" : "merlin.singlerouter",
    "num_ports" : 4
})
comp_net.setSubComponent("topology","merlin.singlerouter")

memctrl0 = sst.Component("memory0", "memHierarchy.MemController")
memctrl0.addParams({
      #"debug" : "1",
      #"debug_level" : 10,
      "backing" : "none",
      "clock" : "1GHz",
      #"backendConvertor.debug_location" : 1,
      #"backendConvertor.debug_level" : 10,
      "backend.access_time" : "50ns",
      "backend.mem_size" : "512MiB",
      "memNIC.network_bw" : "50GB/s",
      "memNIC.addr_range_start" : 0,
      "memNIC.interleave_size" : "128B",
      "memNIC.interleave_step" : "256B",
})
memctrl1 = sst.Component("memory1", "memHierarchy.MemController")
memctrl1.addParams({
      #"debug" : "1",
      #"debug_level" : 10,
      "backing" : "none",
      "backend.access_time" : "50ns",
      "clock" : "1GHz",
      "backend.mem_size" : "512MiB",
      "memNIC.network_bw" : "50GB/s",
      "memNIC.addr_range_start" : 128,
      "memNIC.interleave_size" : "128B",
      "memNIC.interleave_step" : "256B"
})

# Enable statistics
sst.setStatisticLoadLevel(7)
sst.setStatisticOutput("sst.statOutputConsole")
for a in componentlist:
    sst.enableAllStatisticsForComponentType(a)


# Define the simulation links
link_cpu0_l1 = sst.Link("link_cpu0_l1")
link_cpu0_l1.connect( (iface0, "port", "100ps"), (comp_l1_0, "high_network_0", "100ps") )
link_cpu1_l1 = sst.Link("link_cpu1_l1")
link_cpu1_l1.connect( (iface1, "port", "100ps"), (comp_l1_1, "high_network_0", "100ps") )
link_l1_l2_0 = sst.Link("link_l1_l2_0")
link_l1_l2_0.connect( (comp_l1_0, "low_network_0", "100ps"), (comp_l2_0, "high_network_0", "100ps") )
link_l1_l2_1 = sst.Link("link_l1_l2_1")
link_l1_l2_1.connect( (comp_l1_1, "low_network_0", "100ps"), (comp_l2_1, "high_network_0", "100ps") )
link_l2_scratch0 = sst.Link("link_cpu0_scratch0")
link_l2_scratch0.connect( (comp_l2_0, "low_network_0", "100ps"), (comp_scratch0, "cpu", "100ps") )
link_l2_scratch1 = sst.Link("link_cpu1_scratch1")
link_l2_scratch1.connect( (comp_l2_1, "low_network_0", "100ps"), (comp_scratch1, "cpu", "100ps") )
link_scratch0_net = sst.Link("link_scratch0_net")
link_scratch0_net.connect( (comp_scratch0, "network", "100ps"), (comp_net, "port0", "100ps") )
link_scratch1_net = sst.Link("link_scratch1_net")
link_scratch1_net.connect( (comp_scratch1, "network", "100ps"), (comp_net, "port1", "100ps") )
link_mem0_net = sst.Link("link_mem0_net")
link_mem0_net.connect( (memctrl0, "network", "100ps"), (comp_net, "port2", "100ps") )
link_mem1_net = sst.Link("link_mem1_net")
link_mem1_net.connect( (memctrl1, "network", "100ps"), (comp_net, "port3", "100ps") )
# End of generated output.
